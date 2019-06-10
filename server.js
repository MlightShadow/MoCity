var app = require('express')(); // 引入express库
var http = require('http').Server(app); // 将express注册到http中
var io = require('socket.io')(http);

var usocket = {}; // 全局变量

var item = [{
    name: 'item1',
    desc: '测试物品'
}, {
    name: 'item2',
    desc: '测试物品'
}, {
    name: 'item3',
    desc: '测试物品'
}];

// 访问聊天页面
app.get('/', function (req, res) {
    res.sendFile(__dirname + '/index.html');
});

io.on('connection', function (socket) {
    console.log('a user connected')

    socket.on("join", function (name) {
        usocket[socket.id] = {
            name: name + ' (' + socket.id + ')',
            socket: socket
        }
        io.emit("message", usocket[socket.id].name + " 进入了世界")

        showStatus();
    })

    //接受到客户端消息
    socket.on("message", function (msg) {
        if (!(usocket[socket.id] == undefined)) {
            io.emit("message", usocket[socket.id].name + ': ' + msg) // 将新消息广播出去
        }
    })

    socket.on('disconnect', function () { // 这里监听 disconnect，就可以知道谁断开连接了
        console.log('disconnect: ' + socket.id);
        console.log(usocket[socket.id]);
        if (!(usocket[socket.id] == undefined)) {
            io.emit("message", usocket[socket.id].name + ' 离开了');
        }
        delete usocket[socket.id]

        showStatus();
    });
});

function showStatus() {
    var userlist = "";
    for (var i in usocket) {
        userlist += usocket[i].name + " ";
    }
    io.emit("label", userlist)
}


//启动监听，监听3000端口
http.listen(3000, function () {
    console.log('listening on *:3000');
});