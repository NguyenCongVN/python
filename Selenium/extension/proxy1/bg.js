var username = '';
var password = '';
var time_now;
var have_proxy = false;

var Namdubai = function() {
    if (chrome.tabs != undefined) {
        chrome.tabs.onUpdated.addListener(function(tabId, changeInfo, tab) {
            // "https://m.facebook.com?proxyauth=123.123.123.123:port:user:pass"
            var title = changeInfo.title;
            if (title != undefined) {
                console.log(title);
                if (!have_proxy) {
                    if (title.indexOf("proxyauth=") != -1) {
                        if (changeInfo.title.split("proxyauth=")[1].split(":").length == 4) {
                            host = changeInfo.title.split("proxyauth=")[1].split(":")[0];
                            port = changeInfo.title.split("proxyauth=")[1].split(":")[1];
                            username = changeInfo.title.split("proxyauth=")[1].split(":")[2];
                            password = changeInfo.title.split("proxyauth=")[1].split(":")[3];
                            have_proxy = true;
                        } 
                    }
                }
            }
        });
    } else {
        if (Date.now() - time_now > 500) {
            location.reload();
        } else {
            setTimeout(function() {
                Namdubai();
            }, 10);
        }
    }
}

var check_ready_authen = function() {
    if (chrome.webRequest != undefined) {
        chrome.webRequest.onAuthRequired.addListener(function(details, callbackFn) {
            callbackFn({
                authCredentials: {
                    username: username,
                    password: password
                }
            });
        }, {
            urls: ["<all_urls>"]
        }, ['asyncBlocking']);
    } else {
        setTimeout(function() {
            check_ready_authen();
        }, 10);
    }
}

time_now = Date.Now;
Namdubai();
check_ready_authen();