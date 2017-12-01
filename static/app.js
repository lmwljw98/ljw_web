$(function () {
    var i = 6;
    var arr = {{ my|safe }};
    var gif = {{ my2|safe }};
    var mode = 0;

    $("#picture").click(function () {
        $(".row").empty();
        mode = 0;
        for (var j = 0; j < 6; j++) {
            $(".row").append('<div class="col-md-4"><div class="overzoom" style="width:100%; float:left; padding:23px;"><a href="../static/images/' + arr[j] + '" download><img src="../static/images/' + arr[j] + '" class="img-rounded img-responsive" style="width: 100%; height: auto;"></a></div></div>').children(':last').hide().fadeIn(2000);
        }

    });
    $("#gif").click(function () {
        $(".row").empty();
        mode = 1;
        for (var j = 0; j < 6; j++) {
            $(".row").append('<div class="col-md-4"><div class="overzoom" style="width:100%; float:left; padding:23px;"><a href="../static/gif/' + gif[j] + '" download><img src="../static/gif/' + arr[j] + '" class="img-rounded img-responsive" style="width: 100%; height: auto;"></a></div></div>').children(':last').hide().fadeIn(2000);
        }
    });

    $("#reload").after('<br><br>' + arr.length + '장의 대장님<br><br>사진을 클릭하면 다운로드 됩니다.');

    /*
        //모바일 브라우저 문자열 체크
        var UserAgent = navigator.userAgent;
        if (UserAgent.match(/iPhone|iPod|Android|Windows CE|BlackBerry|Symbian|Windows Phone|webOS|Opera Mini|Opera Mobi|POLARIS|IEMobile|lgtelecom|nokia|SonyEricsson/i) != null || UserAgent.match(/LG|SAMSUNG|Samsung/) != null) {
            var mobile = 1;
        }
        else {
            var mobile = 0;
        }
    */

    for (var j = 0; j < 6; j++) {
        $(".row").append('<div class="col-md-4"><div class="overzoom" style="width:100%; float:left; padding:23px;"><a href="../static/images/' + arr[j] + '" download><img src="../static/images/' + arr[j] + '" class="img-rounded img-responsive" style="width: 100%; height: auto;"></a></div></div>').children(':last').hide().fadeIn(2000);
    }

    $(document).scroll(function () {

        var maxHeight = $(document).height();
        var currentScroll = $(window).scrollTop() + $(window).height();

        if (typeof arr[i] != "undefined") {
            if (maxHeight <= currentScroll + 400) {
                if (mode == 0) {

                    $(".row").append('<div class="col-md-4"><div class="overzoom" style="width:100%; float:left; padding:23px;"><a href="../static/images/' + arr[i] + '" download><img src="../static/images/' + arr[i] + '" class="img-rounded img-responsive" style="width: 100%; height: auto;"></a></div></div>').children(':last').hide().fadeIn(2000);
                    $(".row").append('<div class="col-md-4"><div class="overzoom" style="width:100%; float:left; padding:23px;"><a href="../static/images/' + arr[i + 1] + '" download><img src="../static/images/' + arr[i + 1] + '" class="img-rounded img-responsive" style="width: 100%; height: auto;"></a></div></div>').children(':last').hide().fadeIn(2000);
                    $(".row").append('<div class="col-md-4"><div class="overzoom" style="width:100%; float:left; padding:23px;"><a href="../static/images/' + arr[i + 2] + '" download><img src="../static/images/' + arr[i + 2] + '" class="img-rounded img-responsive" style="width: 100%; height: auto;"></a></div></div>').children(':last').hide().fadeIn(2000);
                    $(".row").append('<div class="col-md-4"><div class="overzoom" style="width:100%; float:left; padding:23px;"><a href="../static/images/' + arr[i + 3] + '" download><img src="../static/images/' + arr[i + 3] + '" class="img-rounded img-responsive" style="width: 100%; height: auto;"></a></div></div>').children(':last').hide().fadeIn(2000);
                    $(".row").append('<div class="col-md-4"><div class="overzoom" style="width:100%; float:left; padding:23px;"><a href="../static/images/' + arr[i + 4] + '" download><img src="../static/images/' + arr[i + 4] + '" class="img-rounded img-responsive" style="width: 100%; height: auto;"></a></div></div>').children(':last').hide().fadeIn(2000);
                    $(".row").append('<div class="col-md-4"><div class="overzoom" style="width:100%; float:left; padding:23px;"><a href="../static/images/' + arr[i + 5] + '" download><img src="../static/images/' + arr[i + 5] + '" class="img-rounded img-responsive" style="width: 100%; height: auto;"></a></div></div>').children(':last').hide().fadeIn(2000);
                    $(".row").append('<div class="col-md-4"><div class="overzoom" style="width:100%; float:left; padding:23px;"><a href="../static/images/' + arr[i + 6] + '" download><img src="../static/images/' + arr[i + 6] + '" class="img-rounded img-responsive" style="width: 100%; height: auto;"></a></div></div>').children(':last').hide().fadeIn(2000);
                    $(".row").append('<div class="col-md-4"><div class="overzoom" style="width:100%; float:left; padding:23px;"><a href="../static/images/' + arr[i + 7] + '" download><img src="../static/images/' + arr[i + 7] + '" class="img-rounded img-responsive" style="width: 100%; height: auto;"></a></div></div>').children(':last').hide().fadeIn(2000);
                    $(".row").append('<div class="col-md-4"><div class="overzoom" style="width:100%; float:left; padding:23px;"><a href="../static/images/' + arr[i + 8] + '" download><img src="../static/images/' + arr[i + 8] + '" class="img-rounded img-responsive" style="width: 100%; height: auto;"></a></div></div>').children(':last').hide().fadeIn(2000);
                    $(".row").append('<div class="col-md-4"><div class="overzoom" style="width:100%; float:left; padding:23px;"><a href="../static/images/' + arr[i + 9] + '" download><img src="../static/images/' + arr[i + 9] + '" class="img-rounded img-responsive" style="width: 100%; height: auto;"></a></div></div>').children(':last').hide().fadeIn(2000);
                    $(".row").append('<div class="col-md-4"><div class="overzoom" style="width:100%; float:left; padding:23px;"><a href="../static/images/' + arr[i + 10] + '" download><img src="../static/images/' + arr[i + 10] + '" class="img-rounded img-responsive" style="width: 100%; height: auto;"></a></div></div>').children(':last').hide().fadeIn(2000);
                    $(".row").append('<div class="col-md-4"><div class="overzoom" style="width:100%; float:left; padding:23px;"><a href="../static/images/' + arr[i + 11] + '" download><img src="../static/images/' + arr[i + 11] + '" class="img-rounded img-responsive" style="width: 100%; height: auto;"></a></div></div>').children(':last').hide().fadeIn(2000);

                    i += 12;
                }
                else{
                    $(".row").append('<div class="col-md-4"><div class="overzoom" style="width:100%; float:left; padding:23px;"><a href="../static/gif/' + gif[i] + '" download><img src="../static/images/' + arr[i] + '" class="img-rounded img-responsive" style="width: 100%; height: auto;"></a></div></div>').children(':last').hide().fadeIn(2000);
                    $(".row").append('<div class="col-md-4"><div class="overzoom" style="width:100%; float:left; padding:23px;"><a href="../static/gif/' + gif[i + 1] + '" download><img src="../static/images/' + arr[i + 1] + '" class="img-rounded img-responsive" style="width: 100%; height: auto;"></a></div></div>').children(':last').hide().fadeIn(2000);
                    $(".row").append('<div class="col-md-4"><div class="overzoom" style="width:100%; float:left; padding:23px;"><a href="../static/gif/' + gif[i + 2] + '" download><img src="../static/images/' + arr[i + 2] + '" class="img-rounded img-responsive" style="width: 100%; height: auto;"></a></div></div>').children(':last').hide().fadeIn(2000);
                    $(".row").append('<div class="col-md-4"><div class="overzoom" style="width:100%; float:left; padding:23px;"><a href="../static/gif/' + gif[i + 3] + '" download><img src="../static/images/' + arr[i + 3] + '" class="img-rounded img-responsive" style="width: 100%; height: auto;"></a></div></div>').children(':last').hide().fadeIn(2000);
                    $(".row").append('<div class="col-md-4"><div class="overzoom" style="width:100%; float:left; padding:23px;"><a href="../static/gif/' + gif[i + 4] + '" download><img src="../static/images/' + arr[i + 4] + '" class="img-rounded img-responsive" style="width: 100%; height: auto;"></a></div></div>').children(':last').hide().fadeIn(2000);
                    $(".row").append('<div class="col-md-4"><div class="overzoom" style="width:100%; float:left; padding:23px;"><a href="../static/gif/' + gif[i + 5] + '" download><img src="../static/images/' + arr[i + 5] + '" class="img-rounded img-responsive" style="width: 100%; height: auto;"></a></div></div>').children(':last').hide().fadeIn(2000);
                    $(".row").append('<div class="col-md-4"><div class="overzoom" style="width:100%; float:left; padding:23px;"><a href="../static/gif/' + gif[i + 6] + '" download><img src="../static/images/' + arr[i + 6] + '" class="img-rounded img-responsive" style="width: 100%; height: auto;"></a></div></div>').children(':last').hide().fadeIn(2000);
                    $(".row").append('<div class="col-md-4"><div class="overzoom" style="width:100%; float:left; padding:23px;"><a href="../static/gif/' + gif[i + 7] + '" download><img src="../static/images/' + arr[i + 7] + '" class="img-rounded img-responsive" style="width: 100%; height: auto;"></a></div></div>').children(':last').hide().fadeIn(2000);
                    $(".row").append('<div class="col-md-4"><div class="overzoom" style="width:100%; float:left; padding:23px;"><a href="../static/gif/' + gif[i + 8] + '" download><img src="../static/images/' + arr[i + 8] + '" class="img-rounded img-responsive" style="width: 100%; height: auto;"></a></div></div>').children(':last').hide().fadeIn(2000);
                    $(".row").append('<div class="col-md-4"><div class="overzoom" style="width:100%; float:left; padding:23px;"><a href="../static/gif/' + gif[i + 9] + '" download><img src="../static/images/' + arr[i + 9] + '" class="img-rounded img-responsive" style="width: 100%; height: auto;"></a></div></div>').children(':last').hide().fadeIn(2000);
                    $(".row").append('<div class="col-md-4"><div class="overzoom" style="width:100%; float:left; padding:23px;"><a href="../static/gif/' + gif[i + 10] + '" download><img src="../static/images/' + arr[i + 10] + '" class="img-rounded img-responsive" style="width: 100%; height: auto;"></a></div></div>').children(':last').hide().fadeIn(2000);
                    $(".row").append('<div class="col-md-4"><div class="overzoom" style="width:100%; float:left; padding:23px;"><a href="../static/gif/' + gif[i + 11] + '" download><img src="../static/images/' + arr[i + 11] + '" class="img-rounded img-responsive" style="width: 100%; height: auto;"></a></div></div>').children(':last').hide().fadeIn(2000);

                    i += 12;
                }
            }
        }

        var maxHeight2 = -1;

        $('.overzoom').each(function () {
            maxHeight2 = maxHeight2 > $(this).height() ? maxHeight2 : $(this).height();
        });

        $('.overzoom').each(function () {
            $(this).height(maxHeight2);
        });

        $('img').flexVerticalCenter();
    })


})