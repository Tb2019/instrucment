cookie_temp = document.cookie
Object.defineProperty(document, 'cookie',{
    set:function (val) {
        debugger;
        cookie_temp = val
        return cookie_temp
    },
    get:function () {
        return cookie_temp
    }
})