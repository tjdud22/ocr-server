function logout(){

        $.ajax({
            "url": `/api/v1/users/logout`,
            "method": "POST",
            "timeout": 0,
            "headers": {
            "Content-Type": "application/json",
            'X-CSRFToken': csrftoken
        },
        }).done(function (response) {
        console.log("response : ", response);

        if (response.logout === 'success') {
            location.href = '/mypage';
            console.log("성공")
        } else {
            alert("로그아웃 불가.");
            location.href = '/login';
        }
    }).fail(function (error) {
        console.log("error : ", error);
    })





}