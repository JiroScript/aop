const lowerCaseWords = ["and", "but", "or", "in", "excluding"];

// アンダースコアをスペースに置換します
export function conversion(locationText) {
    let replacedLocation = locationText.replace(/_/g, ' ');

    // スペースで分割して配列にします
    let words = replacedLocation.split(' ');

    // 変換した各単語を保存する配列を作成します
    let processedWords = [];

    // 各単語に対して処理を行います
    words.forEach((word, index) => {
        // 単語がlowerCaseWordsに含まれているかどうかをチェックします
        if (lowerCaseWords.includes(word) && index !== 0) {
            // 単語がlowerCaseWordsに含まれていれば、そのまま保存します
            processedWords.push(word);
        } else {
            // 単語がlowerCaseWordsに含まれていなければ、最初の文字を大文字に変換して保存します
            let capitalizedWord = word.charAt(0).toUpperCase() + word.slice(1);
            processedWords.push(capitalizedWord);
        }
    });

    // 変換した単語をスペースで結合します
    let text = processedWords.join(' ');

    // 最終的なテキストをセットします
    return text;
    }

// select要素の子にoption要素を生成します。
export function createOption(locationSelect, locations) {
    locations.forEach(location => {
        const optionElement = document.createElement('option');
        optionElement.value = location;
        optionElement.textContent = conversion(location);
        locationSelect.appendChild(optionElement);
      });    
    }
    
// URL「書き換え」
export function URLrewriting(hash){
    // クエリー引数の変更
    let params = new URLSearchParams(window.location.search); 
    Object.keys(hash).forEach(key => {
        ( key + ':' + hash[key])
        params.set(key, hash[key]);
    })
    window.location.origin + window.location.pathname + '?' + params.toString(); // エラーがおこる
    let newUrl = '?' + params.toString();
    
    // URL「書き換え」。パラメータに反映させる
    window.history.pushState({}, '', newUrl);
}

export function getHostName(){
   
    try{
        const os = require('os');
        const HostName = os.hostname();
        console.log(`Node.js環境 ${HostName}`);
        return HostName;
    }catch(err){
        const HostName = window.location.hostname;
        (err.name + ': ' + err.message);
        (`ブラウザ環境 ${HostName}`);
        return HostName;
    }
 
}