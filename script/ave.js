// 総人口
export function Populationfic(rawData, rank, i) {
    const population = rawData.reduce(function(sum, d) { return sum + d.total; }, 0);

    // <h2>に<small class="headline">と<span class="population">を生成
    createElements(i, "population", population.toLocaleString())
    }

    
// 平均年齢
export function averageAge(rawData, rank, i) {
    rawData.forEach(function(obj) {
        obj.value = obj.total; //プロパティを指定、値を追加、
        delete obj.value; //オブジェクトを削除
        });
    // 各年齢層の中央値を計算
    function getMidpoint(ageRange) {
        if (ageRange === "100+") {
        return null;
        }
        
        var [minAge, maxAge] = ageRange.split("_").map(Number);
    return (minAge + maxAge) / 2;
    }

    // 年齢層ごとの人口に中央値を掛けた値を計算し、合計を求める
    var weightedSum = rawData.reduce(function (sum, d) {
        var midpoint = getMidpoint(d.age);
        
            if (midpoint === null) {
            return sum;
            }
        
        return sum + midpoint * (d.total);
    }, 0);

    // 全人口を求める
    var totalPopulation = rawData.reduce(function (sum, d) {
        return sum + d.total;
    }, 0);

    // 平均年齢を計算
    var averageAge = weightedSum / totalPopulation;
    
    averageAge.toFixed(1); // 小数点第一位に丸める
    
    // <h2>に<small class="headline">と<span class="average-age">を生成
    createElements(i, "average-age", averageAge.toFixed(1))

    } // function


// <h2>に<small class="headline">と<span class="">を生成
function createElements(i, classname, value){
    var sections = document.querySelectorAll('.sect');
    var h2 = sections[i].querySelector('h2.population_average');
    var span = h2.querySelector('span.'+ classname);
    (h2.childNodes)
    if(span){
      span.textContent = value;
    }else{ // null
      var small = document.createElement('small');
      small.textContent = classname;
      small.className = "headline"; // classを設定
      h2.appendChild(small);
      var span = document.createElement('span');
      span.textContent = value;
      span.className = classname; // classを設定
      h2.appendChild(span);
    }
    
}


// 要素の削除
export function deleteElements(rank, i) {
    var sections = document.querySelectorAll('.sect');
    var h2 = sections[i].querySelector('h2.population_average');

    // small
    var NodeLists = h2.querySelectorAll('small');
    // NodeListを走査します。
    NodeLists.forEach(elm => {
        elm.classList.remove('headline'); // classのみ削除, sample
        elm.remove('small');
    });

    // span
    var NodeLists = h2.querySelectorAll('span');
    NodeLists.forEach(elm => {
        elm.remove('span');
    });

    // svg
    var div = sections[i].querySelector('div.' + rank);
    const svg = div.querySelector('svg');
        if (svg) {
        div.removeChild(svg);
        }

}