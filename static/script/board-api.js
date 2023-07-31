const board_number = window.location.pathname.split('/board/')[1]

$.ajax({
    "url": `/api/v1/boards/board/${board_number}`,
    "method": "GET",
    "timeout": 0,
}).done(function (board) {
    console.log(board);
    $('#author').text(board.author === null ? 'anonymous' : board.author.username);
    $('#title').val(board.title);
    $('#contents').val(board.contents);
    $('#loaded_file').attr('src', board.image_url);
    console.log("url : ", board.image_url)
    $('#created_at').val(board.created_at);
    $('#modified_at').val(board.modified_at);

    
    var langpack = $('#langpack');


    if (board.image_url) {
      langpack.show()
    }else{
        langpack.hide()
    }



});




