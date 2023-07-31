$.ajax({
    "url": "/api/v1/boards",
    "method": "GET",
    "timeout": 0,
}).done(function (list) {
    list.forEach(board => {
        image_url = board.image_url;
        // image_url = board.loaded_file === null ? image_url : board.loaded_file;
        
        $('#boards-container').append(`
        <div class="board">
    
                <img src="${image_url}">
                <p>
                    <a href="/board/${board.no}"><h4>${board.title}</h4></a>
                    <span>${board.author === null ? 'anonymous' : board.author.username}</span>
                </p>
            </div>
        `)
    })
});