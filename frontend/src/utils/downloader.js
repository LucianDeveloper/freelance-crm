import rawApi from "./rawApi";

const download = (url) => {
    rawApi(url, {}, true).then((response) => {
        downloader(response, `file.${url.split('.').reverse()[0]}`)
    })
}


const downloader = (response, name) => {
    response.blob().then(blob => {
        downloaderBlob(blob, name)
    })
}

const downloaderBlob = (blob, name) => {
    let url = window.URL.createObjectURL(blob);
    let a = document.createElement('a');
    a.href = url;
    a.download = name;
    a.click();
}

export {download, downloader, downloaderBlob}