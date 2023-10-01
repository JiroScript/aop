// element
import { Regionals, countries, RegionsCountries, worlds, regions, develops, incomes} from './arr.js';
import {createOption, conversion } from './func.js';

// 次に、<select> タグを取得します。ここではその id が 'locationSelect' だと仮定します
const selectElement = document.getElementById('locationSelect');
// 配列の各場所について、新たな <option> 要素を作成し、それを <select> タグに追加します
createOption(selectElement, countries().sort());

// section要素に配色
const selection = d3.selectAll( "section" );
// selection要素にデータが割り当て
selection.data(["#010101", "#020202", "#030303", "#040404"]) 
    .style( "color", function(d) { return d; });

/**/
// select要素への参照を取得
var select = document.querySelector('select[name="regions"]');
// 各大州および小地域のデータ
var regionsData = Regionals()

// データを元にoptgroupとoptionを作成し、selectに追加
for (var Region in regionsData) {
    var optgroup = document.createElement('optgroup');
    optgroup.label = Region;
    regionsData[Region].forEach(function(subRegion) {
        var option = document.createElement('option');
        option.value = subRegion;
        option.innerText = subRegion;
        optgroup.appendChild(option);
    });
    select.appendChild(optgroup);
}

//
// 提案された以前のコードに続く部分

var selectCountry = document.querySelector('select[id="locationSelect"]');

select.addEventListener('change', function() {
    // 以前の国のオプションをクリア
    var currentSelectedCountry = selectCountry.value;
    selectCountry.innerHTML = "";

    // 選択された小地域の国のリストを取得
    const selectedRegion = this.value; // Eastern Asia
    
    const countriesHush = { ...{"Abc Order": countries().sort()},
    ...RegionsCountries(),  
    ...{"World": worlds()}, 
    ...{"Region": regions().sort()},
    ...{"Develop": develops().sort()}, 
    ...{"Income": incomes().sort()} 
    };
    console.log(countriesHush);
    const countriesList = countriesHush[selectedRegion];
    (RegionsCountries()[selectedRegion]);
    countriesList.unshift(currentSelectedCountry);
    creation( countriesList, 'option');

});

function creation(l, elements) {
        l.forEach(function(country) {
            var option = document.createElement(elements);
            option.value = country;
            option.innerText = conversion(country);
            selectCountry.appendChild(option);
        });

}