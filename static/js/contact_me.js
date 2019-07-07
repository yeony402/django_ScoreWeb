$(function() {

  $("#contactForm input,#contactForm textarea").jqBootstrapValidation({
    preventSubmit: true,
    submitError: function($form, event, errors) {
      // additional error messages or events
    },
    submitSuccess: function($form, event) {
      event.preventDefault(); // prevent default submit behaviour
      // get values from FORM
      var name = $("input#name").val();
      var email = $("input#email").val();
      var phone = $("input#phone").val();
      var message = $("textarea#message").val();
      var firstName = name; // For Success/Failure Message
      // Check for white space in name for Success/Fail message
      if (firstName.indexOf(' ') >= 0) {
        firstName = name.split(' ').slice(0, -1).join(' ');
      }
      $this = $("#sendMessageButton");
      $this.prop("disabled", true); // Disable submit button until AJAX call is complete to prevent duplicate messages
      $.ajax({
        url: "././mail/contact_me.php",
        type: "POST",
        data: {
          name: name,
          phone: phone,
          email: email,
          message: message
        },
        cache: false,
        success: function() {
          // Success message
          $('#success').html("<div class='alert alert-success'>");
          $('#success > .alert-success').html("<button type='button' class='close' data-dismiss='alert' aria-hidden='true'>&times;")
            .append("</button>");
          $('#success > .alert-success')
            .append("<strong>Your message has been sent. </strong>");
          $('#success > .alert-success')
            .append('</div>');
          //clear all fields
          $('#contactForm').trigger("reset");
        },
        error: function() {
          // Fail message
          $('#success').html("<div class='alert alert-danger'>");
          $('#success > .alert-danger').html("<button type='button' class='close' data-dismiss='alert' aria-hidden='true'>&times;")
            .append("</button>");
          $('#success > .alert-danger').append($("<strong>").text("Sorry " + firstName + ", it seems that my mail server is not responding. Please try again later!"));
          $('#success > .alert-danger').append('</div>');
          //clear all fields
          $('#contactForm').trigger("reset");
        },
        complete: function() {
          setTimeout(function() {
            $this.prop("disabled", false); // Re-enable submit button when AJAX call is complete
          }, 1000);
        }
      });
    },
    filter: function() {
      return $(this).is(":visible");
    },
  });

  $("a[data-toggle=\"tab\"]").click(function(e) {
    e.preventDefault();
    $(this).tab("show");
  });
});

/*When clicking on Full hide fail/success boxes */
$('#name').focus(function() {
  $('#success').html('');
});



// 하단에 학교 홈페이지를 새창으로 열기
$('.cku').click(function() {
   window.open("http://www.cku.ac.kr/mbshome/mbs/CKU/index.do");
 });





// 자동합계 - document_post.html
$(function(){

  $('input.num_only').on('keyup', function(){
    var cnt = $(".total input.num_sum").length;
    console.log(cnt);

    for(var i=1; i<cnt; i++){
      var sum = parseInt($(this).val() || 0);
      sum++
      console.log(sum);
    }

    var s1 = parseInt($("#id_score_0").val() || 0);
    var s2 = parseInt($("#id_score_1").val() || 0);
    var s3 = parseInt($("#id_score_2").val() || 0);
    var s4 = parseInt($("#id_score_3").val() || 0);
    var s5 = parseInt($("#id_score_4").val() || 0);
    var s6 = parseInt($("#id_score_5").val() || 0);
    var s7 = parseInt($("#id_score_6").val() || 0);
    var s8 = parseInt($("#id_score_7").val() || 0);
    var pf = parseFloat($("#id_plus_points").val());

    var subsum_1 = s1+s2;
    var subsum_2 = s3+s4;
    var subsum_3 = s5+s6;
    var subsum_4 = s7+s8;
    var sum = s1+s2+s3+s4+s5+s6+s7+s8+pf;
    // console.log(subsum);
    $("#subsum_1").val(subsum_1);
    $("#subsum_2").val(subsum_2);
    $("#subsum_3").val(subsum_3);
    $("#subsum_4").val(subsum_4);
    $("#sum").val(sum);
  });



  // 점수 입력창 저장 함수 - 입력숫자 범위 확인하기
//   $('tbody').on('submit', '#scoreform', function(){
//     var score_0 = parseInt($("#id_score_0").val());
//     var score_1 = parseInt($("#id_score_1").val());
//     var score_2 = parseInt($("#id_score_2").val());
//     var score_3 = parseInt($("#id_score_3").val());
//     var score_4 = parseInt($("#id_score_4").val());
//     var score_5 = parseInt($("#id_score_5").val());
//     var score_6 = parseInt($("#id_score_6").val());
//     var score_7 = parseInt($("#id_score_7").val());
//
//     if(score_0 > 15) {
//       alert("1-1번 점수를 확인해주세요.");
//       return false;
//     } else if(score_1 > 15 || score_1 < 0) {
//       alert("1-2번 점수를 확인해주세요.");
//       return false;
//     } else if(score_2 > 15 || score_2 < 0) {
//       alert("2-1번 점수를 확인해주세요.");
//       return false;
//     } else if(score_3 > 15 || score_3 < 0) {
//       alert("2-2번 점수를 확인해주세요.");
//       return false;
//     } else if(score_4 > 5 || score_4 < 0) {
//       alert("3-1번 점수를 확인해주세요.");
//       return false;
//     } else if(score_5 > 10 || score_5 < 0) {
//       alert("3-2번 점수를 확인해주세요.");
//       return false;
//     } else if(score_6 > 10 || score_6 < 0) {
//       alert("4-1번 점수를 확인해주세요.");
//       return false;
//     } else if(score_7 > 10 || score_7 < 0) {
//       alert("4-2번 점수를 확인해주세요.");
//       return false;
//     } else if(confirm("저장하시겠습니까?")) {
//       alert("저장되었습니다.");
//       return true;
//     } else {
//       alert("취소되었습니다.");
//       return false;
//     }
//   });
//
// });

  $(document).ready(function(){
    try{
      $("#scoreform").submit(function(){
        var s1 = parseInt($("#id_score_0").val() || 0);
        var s2 = parseInt($("#id_score_1").val() || 0);
        var s3 = parseInt($("#id_score_2").val() || 0);
        var s4 = parseInt($("#id_score_3").val() || 0);
        var s5 = parseInt($("#id_score_4").val() || 0);
        var s6 = parseInt($("#id_score_5").val() || 0);
        var s7 = parseInt($("#id_score_6").val() || 0);
        var s8 = parseInt($("#id_score_7").val() || 0);
        // var score_0 = $('#score_0')[0];
        if(confirm("저장하시겠습니까?")){
          if(s1 > 15){
            alert("1-1번 점수를 확인해주세요.");
            return false;
          } else if(s2 > 15 || s2 < 0){
            alert("1-2번 점수를 확인해주세요.");
            return false;
          } else if(s3 > 15 || s3 < 0){
            alert("2-1번 점수를 확인해주세요.");
            return false;
          } else if(s4 > 15 || s4 < 0){
            alert("2-2번 점수를 확인해주세요.");
            return false;
          } else if(s5 > 5 || s5 < 0){
            alert("3-1번 점수를 확인해주세요.");
            return false;
          } else if(s6 > 10 || s6 < 0){
            alert("3-2번 점수를 확인해주세요.");
            return false;
          } else if(s7 > 10 || s7 < 0){
            alert("4-1번 점수를 확인해주세요.");
            return false;
          } else if(s8 > 10 || s8 < 0){
            alert("4-2번 점수를 확인해주세요.");
            return false;
          } else{
            alert("저장되었습니다.");
            return True;
          }
        }
        else{
          alert("취소되었습니다.");
          return false;
        }
      });
    }
    catch(exception){
      alert("점수를 확인해주세요.");
    }
  });
});


//전체 점수결과 합계 나타내기 - https://stackoverflow.com/questions/22536448/jquery-sum-rows-adding-all-cells
// 템플릿태그에서 id name으로 실행시키면 첫째라인의 합계가 안나오는데 class name으로 실행시키면 정상작동함. **알아보기
$(document).ready(function () {
    //iterate through each row in the table
    $('table tbody tr').each(function () {
        //the value of sum needs to be reset for each row, so it has to be set inside the row loop
        var sum = 0
        //find the combat elements in the current row and sum it
        $(this).find('.id_score').each(function () {
            var id_score = $(this).text();
            if (!isNaN(id_score) && id_score.length !== 0) {
                sum += parseFloat(id_score);
            }
        });
        //set the value of currents rows sum to the total-combat element in the current row
        $('.sum', this).html(sum);
    });
});





// 지원자 기본정보 저장 함수
$(document).ready(function(){
  $("#ceoform").submit(function(){
    if (confirm("저장하시겠습니까?")) {
      alert("저장되었습니다.");
      return true;
    }
    else{
       alert("취소되었습니다.");
       return false;
     }
  });
});


// // 점수 입력창 저장 함수
// $(document).ready(function(){
//   $("#scoreform").submit(function(){
//     if (confirm("저장하시겠습니까?")) {
//       alert("저장되었습니다.");
//       return true;
//     }
//     else{
//        alert("취소되었습니다.");
//        return false;
//      }
//   });
// });







// 정보 수정 함수 - 위의 저장함수보고 폼 유효성 검사 부분 추가하기
function changeFunction() {
  if (confirm("수정하시겠습니까?")) {
   alert("수정되었습니다.");
   return true;
 }
 else{
   alert("취소되었습니다.");
   return false;
    }
  }

function notexist(){
  alert("존재하지 않는 데이터입니다.")
}
