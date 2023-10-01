//
export function BarPercentageUpdate(sct, population, rawData, rank, i){

    var margin = {top: 20, right: 70, bottom: 30, left: 60},
    area = {width: 550 - margin.left - margin.right, height: 400 - margin.top - margin.bottom};
    // 目盛りの設定
    var y = scale(area, rawData).Y, x = scale(area, rawData).X;
    let div = sct.querySelector('div.'+ rank);

    // SVG要素が存在する場合と存在しない場合で処理を分岐
    if (!!div.querySelector('svg')) { // 論理否定演算子でnullを判定する
        UpdateGraph(y, x, population, rawData, rank, i);
    } else {
        DrawGraph(y, x, margin, area, population, rawData, rank, i);
        UpdateGraph(y, x, population, rawData, rank, i);
    }
}

// 目盛りの設定
function scale(area, rawData){    
    
    // y軸
    var y = d3.scaleBand()
        .range([area.height, 0])
        .domain(rawData.map(function(d) { return d.age; })) // 0_4 5_9 10_14
        .padding(0.0);

    // x軸
    var x = d3.scaleLinear() // 
        .range([0, area.width]) // 画面上のpxの範囲
        .domain([0, 0.20]); // 最小・最大20%,  domain:縄張り, 領域, 

    return {Y: y, X: x};
}
//
function DrawGraph(y, x, margin, area, population, rawData, rank, i) {
// ここで「各年代の人口比率の最大値」を計算します
var maxRatio = d3.max(rawData, function(d) { return d.total / population; });

var svg = d3.select("div." + rank)
    .append("svg") // svg要素を作成
    .attr("class", rank)
    .attr("width", area.width + margin.left + margin.right)
    .attr("height", area.height + margin.top + margin.bottom)
    .append("g")
    .attr("transform", "translate(" + margin.left + "," + margin.top + ")");

    // Y軸を作成
    var yAxis = d3.axisLeft(y)
        .tickSize(1)
        .tickPadding(10);
        
    svg.append("g")
        .call(yAxis)
        .selectAll("text")
        .style("font-size", "1em"); // Y軸目盛りのフォントサイズを設定

    // X軸を作成(座標軸)
    var xAxis = d3.axisBottom(x)
        .tickFormat(d3.format(".1%"))
        .tickSize(2)
        .tickPadding(10);
        
    svg.append("g")
        .attr("transform", "translate(0," + area.height + ")")
        .call(xAxis)
        .selectAll("text")
        .style("font-size", "1em"); // X軸目盛りのフォントサイズを設定
}

function UpdateGraph(y, x, population, rawData, rank, i) {
    
    // Tooltip divを作成 対象の要素にカーソルを合わせた時に小さな領域を表示するJavascriptです。
    var tooltip = d3.select("div." + rank)
        .append("div")	
        .attr("class", "tooltip")				
        .style("opacity", 0);

    var g = d3.select("div." + rank).select("svg").select("g");
    //
    var bars = g.selectAll(".bar").data(rawData);
    barz(y, x, bars, rawData, population, tooltip);
    //
    var texts = g.selectAll(".text").data(rawData);
    textz(y, x, texts, population);
    //
    var percentage = g.selectAll(".percentage-text").data(rawData);
    percentagez(y, x, percentage, rank, population);

}

function barz(y, x, bars, rawData, population, tooltip){
    bars.exit().remove();
    // create new bars
    bars.enter()
        .append("rect")
        .attr("class", "bar")
        .attr("y", function(d) { return y(d.age); })
        .attr("x", 0)
        .attr("height", y.bandwidth()) 
        .attr("fill", function(d, i) { return d3.interpolateGreys(i / rawData.length + 0.4); })
        .on("mouseover", function(event, d) {
            tooltip.transition()		
                .duration(100)		
                .style("opacity", .9);
            tooltip.html(d.total.toLocaleString())	
                .style("left", (event.pageX) + "px")		
                .style("top", (event.pageY - 28) + "px");	
        })					
        .on("mouseout", function(d) {		
            tooltip.transition()		
                .duration(100)		
                .style("opacity", 0);	
        })
        .transition()
        .duration(0) // アニメーションにかかる時間を指定する
        .attr("width", function(d) { return x(d.total / population); });

    // Barにマウスオーバーとマウスアウトのイベントを追加
    bars.on("mouseover", function(event, d) {
            tooltip.transition()		
                .duration(100)		
                .style("opacity", .9);
            tooltip.html(d.total.toLocaleString())	
                .style("left", (event.pageX) + "px")		
                .style("top", (event.pageY - 28) + "px");	
        })					
        .on("mouseout", function(d) {		
            tooltip.transition()		
                .duration(100)		
                .style("opacity", 0);	
        });

    bars.transition()
        .duration(0) // アニメーションにかかる時間を指定する
        .attr("width", function(d) { return x(d.total / population); });
}
function textz(y, x, texts, population){
    texts.exit().remove();

    // Update existing texts
    texts.transition()
        .duration(0)
        .attr("y", function(d) { return y(d.age) + y.bandwidth() / 2; })
        .attr("x", function(d) { return x(d.total / population) + 5; })
        .text(function(d) { return d.total; });
    
    // Create new texts
    texts.enter()
        .append("text")
        .attr("class", "text")
        .attr("y", function(d) { return y(d.age) + y.bandwidth() / 2; })
        .attr("dy", ".35em")
        .attr("x", 5)
        .attr("text-anchor", "start")
        .text(function(d) { return d.total; })
        .attr("fill", "none"); // 追加：一時的にfillをnoneに設定
    
    texts.transition()
        .duration(0) // アニメーションにかかる時間を指定する
        .attr("x", function(d) { return x(d.total / population) + 5; });
    

}
function percentagez(y, x, percentage, rank, population){
    percentage.exit().remove();
    var percentageFormat = d3.format(".1%");
    // Update existing percentage texts
    percentage.transition()
        .duration(0)
        .attr("y", function(d) { return y(d.age) + y.bandwidth() / 2; })
        .attr("x", function(d) { return x(d.total / population) + 5 + getTextWidth(d.total, 0) + 0; })
        .text(function(d) { return percentageFormat(d.total / population); });
    
    // Create new percentage texts
    percentage.enter()
        .append("text")
        .attr("class", "percentage-text")
        .attr("y", function(d) { return y(d.age) + y.bandwidth() / 2; })
        .attr("x", function(d) { return x(d.total / population) + 5 + getTextWidth(d.total, 0) + 0; })
        .attr("dy", ".35em")
        .attr("text-anchor", "start")
        .text(function(d) { return percentageFormat(d.total / population); });
        
        percentage.transition()
            .duration(0) // アニメーションにかかる時間を指定する
            .attr("x", function(d) { return x(d.total / population) + 5 + getTextWidth(d.total, 0) + 0; });
    
    // 他のコードの前に、新しい関数を定義します
    function getTextWidth(text, fontSize) {
        var svg = d3.select("div." + rank).append("svg");
        var textElement = svg.append("text").attr("font-size", fontSize).text(text);
        var width = textElement.node().getBBox().width;
        svg.remove();
        return width;
        }
}

// #################################