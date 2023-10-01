// npm とは · Node Package Manager の略。 · JavaScript 系のパッケージを管理するツール。
    
import {URLrewriting, getHostName} from './func.js';
import {BarPercentageUpdate} from './gp.js';
import {averageAge, Populationfic, deleteElements} from './ave.js';
import {ChipStyle} from './chi.js';

(window.location.href, Boolean(window.location.search))
// Dateをコンストラクタとして呼び出す
const now = new Date();
const ThisYear = now.getFullYear() // 今年

const HostName = getHostName() // 127.0.0.1

export const fetchAc = (location, year) => {
    const isFuture = year > ThisYear;
    // chip
    ChipStyle(isFuture);
    const arr = ['total', 'low', 'medium', 'high'];
    arr.forEach(function(rank, i) { // 関数式（関数リテラル）

        /*
        fetch('http://127.0.0.1:3000/' + rank + '?location=' + location )
        fetch('http://localhost:3000/' + rank + '?location=' + location )
        fetch('http://tk*.ne.jp:3000/' + rank + '?location=' + location ) */
        fetch('http://' + HostName + ':3000/' + rank + '?location=' + location )
        .then(response => response.json())
        .then(ObjectLiteral => {

        // total以外のデータを調整。
        // yearに該当するデータを抽出。
        const obj = ObjectLiteral.filter(obj => obj.year == year);
        if (rank == 'total'){
            var rawData = obj;
        }else{
            var rawData = conditions([], obj);
        }
        // div要素のテキストを更新
        document.getElementById('dataDisplay').textContent = location + ' ' + year;
        //
        (!!Object.keys(rawData).length); // オブジェクトが空ならfalse

        // 総人口
        const population = rawData.reduce(function(sum, d) { return sum + d.total; }, 0);
        let sct = document.querySelector('section.' + rank);

        //  <h2 class="population_average">の<small><span>要素, およびsmg要素の削除・生成・更新・表示
        if(rank == 'total' && isFuture || rank != 'total' && !isFuture){
            // 要素の削除
            deleteElements(rank, i);     
            // section要素にhideクラス追加   
            sct.classList.add('hide');            sct.querySelector('h2').classList.add('hide');
            // div.chip要素のクリック・タッチを無効化・非表示
            //ChipStyle("none", "hidden");

        }else if(rank == 'total' && !isFuture || rank != 'total' && isFuture ){
            // div.chip要素のクリック・タッチを有効化・表示
            //ChipStyle("auto", "visible");
            // div.chip要素にactivクラスを初期設定で追加、その値と合致したrank、及びtotalの場合。 
            if (rank == document.querySelector('div.chip.active').dataset.name || rank == 'total'){
            // section要素のhideクラス削除。
            // クラスを削除することでsection要素が表示される。
            sct.classList.remove('hide');            sct.querySelector('h2').classList.remove('hide');
            }
            // 総人口
            Populationfic(rawData, rank, i);
            // 平均年齢
            averageAge(rawData, rank, i);
            // 棒とパーセンテージの更新。
            BarPercentageUpdate(sct, population, rawData, rank, i);
        }
        
        // URL「書き換え」
        const hash = {'location': location, 'year': year};
        URLrewriting(hash);
        })
        .catch(error => console.error('Error:', error));
    }); // forEach

    // 関数式（関数リテラル）, condition:条件
    const conditions = function(rawData, obj){
        obj.forEach(item => {
            Object.keys(item).forEach(key => {
                if(key !== "index" && key !== "location" && key !== "year"){
                    let newItem = {
                        "index": item.index,
                        "location": item.location,
                        "year": item.year,
                        "age": key,
                        "total": item[key] * 1000
                    }
                    rawData.push(newItem);
                }
            })
        })
        return rawData;
    }
}; // fachAc


