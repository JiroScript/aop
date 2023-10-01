// parameter
const locationSelect = document.getElementById('locationSelect');
const yearInput = document.getElementById('year');
const chips = document.querySelectorAll('div.chip');

import {createOption} from './func.js';
import {fetchAc} from './fh.js';

(window.location.href, Boolean(window.location.search))
// Dateをコンストラクタとして呼び出す
const now = new Date();
const ThisYear = now.getFullYear() // 今年

// activeクラスを設定する関数
function setActive(NodeListIndex) {
    // すべてのchip要素のactiveクラスを削除
    Array.from(chips).forEach(elm => elm.classList.remove('active')); 
    // chip要素にactiveクラスを追加
    document.querySelector(`#chip-container .chip:nth-child(${NodeListIndex + 1})`).classList.add('active');
}

// parameter not in URL
if (!window.location.search){
    // select要素にoption要素を生成
    createOption(locationSelect, ['world']);  
    yearInput.value = ThisYear;

    // chip要素にactiveクラスをセット
    setActive(0);

    // 指定されたNodeListから、activeクラスを含む要素のオブジェクトを返す
    const ActiveChip = Array.from(chips).find(chip => chip.classList.contains('active'));

    // 要素の値を取得, クエリ作成
    const newUrl = '?location=' + locationSelect.value + '&year=' + yearInput.value + '&rank=' + ActiveChip.dataset.name;
    // URLにクエリを追加 
    window.history.pushState({}, '', newUrl);

// parameter in URL
}else if(!!window.location.search){
    // URLからパラメータを取得、
    const params = new URLSearchParams(window.location.search);
    // 変数に代入
    const location = params.get('location'), year = params.get('year'), rank = params.get('rank'); // "world", "2020", 'low'
    createOption(locationSelect, [location]); // select要素にoption要素を生成
    yearInput.value = year;

    // 
    const NodeListIndex = Array.from(chips).findIndex(chip => chip.dataset.name == rank); // 1

    // chip要素にactiveクラスをセット
    setActive(NodeListIndex);
}

// ページロード時にデフォルトのlocationとyearでデータをフェッチ
fetchAc(locationSelect.value, yearInput.value);

// locationが変更されたときにデータを再フェッチ
locationSelect.addEventListener('change', () => {
    fetchAc(locationSelect.value, yearInput.value);
});

yearInput.addEventListener('input', () => {
    fetchAc(locationSelect.value, yearInput.value);
});

const operations = [
    { id: 'minusTen', value: -10 },
    { id: 'minus', value: -1 },
    { id: 'plus', value: 1 },
    { id: 'plusTen', value: 10 }
];

// <input type="button">が押下されたときにデータを再フェッチ
for (let operation of operations){
    document.getElementById(operation.id).addEventListener('click', function() {
        let newValue = parseInt(yearInput.value) + operation.value;
        if (newValue >= parseInt(yearInput.min) && newValue <= parseInt(yearInput.max)) {
            yearInput.value = newValue;
            fetchAc(locationSelect.value, yearInput.value);
        }
    });
}
