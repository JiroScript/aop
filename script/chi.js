import {URLrewriting} from './func.js';

export function ChipStyle(isFuture){
    const container = document.getElementById("chip-container");
    container.style.pointerEvents = isFuture ? "auto" : "none";
    container.style.visibility = isFuture ? "visible" : "hidden";
}


export function NodeListSetObjectClear(SetObject, chips){
    SetObject.clear(); 
    Array.from(chips).forEach(elm => elm.classList.remove('active'));
}
function choice_chips(){ 
    const chips = document.querySelectorAll('.chip');  // NodeList(3) [div.chip, div.chip.active, div.chip]
    // Setオブジェクト:forEach() メソッドによく用いられます。重複した値がないことを保証したコレクション。
    const SetObject = new Set(); // Set(0) {size: 0}
    const params = new URLSearchParams(window.location.search);
    const rank = params.get('rank'); // 'low'
    SetObject.add( rank); 

    chips.forEach(chip => {
        chip.addEventListener('click', (event) => {
            const chipElement = event.target; // <div class="chip activ" >Low</div>
            const chipValue = chipElement.getAttribute('data-name'); // 'low'
            (chipValue)

            // Clear all previously selected chips
            NodeListSetObjectClear(SetObject, chips);

            SetObject.add(chipValue);
            chipElement.classList.add('active'); // クラスを追加する。
            
            (Array.from(SetObject)); // ['medium']
            // Set(1) {'medium'}
            AddClasse(SetObject);

            // URL「書き換え」            
            const newValue = Array.from(SetObject).join(', '); // URLのパラメータに反映させる
            const hash = {'rank': newValue};
            URLrewriting(hash);
        });
    });
}

//
function filter_chips(){ 
    const chips = document.querySelectorAll('.chip');
    // Setオブジェクト:forEach()メソッドによく用いられます。重複した値がないことを保証したコレクション。
    const SetObject = new Set(); // Set(0) {size: 0}
            
    Array.from(chips).forEach(elm => {  (elm.dataset.name)  });
            // 
    chips.forEach(chip => {
        chip.addEventListener('click', (event) => {
            const chipElement = event.target; // <div class="chip activ" data-value="chip1">Low</div>
            const chipValue = chipElement.getAttribute('data-name'); // 'total'

            (SetObject, chipElement, chipValue)

            if (SetObject.has(chipValue)) { // has():その値がSetオブジェクトに存在するかどうかを確認できます。
                SetObject.delete(chipValue);
                chipElement.classList.remove('active'); // クラスを削除する。
            } else {
                SetObject.add(chipValue);
                chipElement.classList.add('active'); // クラスを追加する。
            }
            
            (Array.from(SetObject)); // ['total']
            // Set(3) {'low', 'medium', 'high'}
            AddClasses(SetObject);
        });
    });
}

function AddClasse(SetObject){
    (SetObject) // Set(3) {'low', 'medium', 'high'}

    //section要素のクラスを取得
    let uniqueClasses = getClass('section');
    // 'sect', 'hide', 'total' を排除
    let filteredClasses = uniqueClasses.filter(className => { 
        return className !== 'sect' && className !== 'hide' && className !== 'total';
    });
    filteredClasses.forEach(elm => { 
        // section要素のhideクラス削除 
        let sct = document.querySelector('section.' + elm);
        sct.classList.add('hide');            sct.querySelector('h2').classList.add('hide');
        });
    
    SetObject.forEach(elm => {
        (document.querySelector('section.' + elm));
        // section要素にhideクラス追加   
        let sct = document.querySelector('section.' + elm);
        sct.classList.remove('hide');            sct.querySelector('h2').classList.remove('hide');
    });
}

//
function getClass(element){ // すべてのsection要素を取得
    let sections = document.querySelectorAll(element);
    let classesArray = [];
    sections.forEach(section => {
        // 各sectionのクラスリストを取得し、それを配列に変換
        let classList = Array.from(section.classList);
        classesArray = classesArray.concat(classList);
    });
    // 重複するクラスを排除
    let uniqueClasses = [...new Set(classesArray)];
return uniqueClasses;
}

//filter_chips();
choice_chips();