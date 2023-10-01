/*pp:ポートフォリオ*/

/*  reduce() 
配列データの各要素を累積して1つの値にする用途に最適なメソッド*/
var x = [" ", "world", "!"].reduce(function(sum, str){ return sum + str; }, "hello"); // hello world!
(x)

/* 
map()
配列に対して処理できるメソッド何らかの処理を行った結果を新しい配列として生成できる
*/
var numbers = [1,2,3,4,5];

var result = numbers.map(function(num) {
return num * 2;
})

result; // [2, 4, 6, 8, 10]

document.addEventListener('DOMContentLoaded', function(){
    ('DOMContentLoaded');
});

//
var nodes = document.querySelectorAll('div.chip');
// 指定されたNodeListから、activeクラスを含む要素のインデックスを返す
const activeIndex = Array.from(nodes).findIndex(chip => chip.classList.contains('active'));
(activeIndex);