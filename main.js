$(document).ready(function(){


	$('.container').show()
	refreshPunchline()
	$('.leftchoice img').click(function(){
		$('.leftchoice img').removeClass('selected')
		$(this).addClass('selected')
	})
	$('.rightchoice img').click(function(){
		$('.rightchoice img').removeClass('selected')
		$(this).addClass('selected')
	})

	$('#generer_button .btn').click(function(){
		refreshPunchline()
	})

	function refreshPunchline(r1="Orelsan",r2="Damso") {
		r1 = $('.leftchoice .selected').attr('id').substr(1)
		r2 = $('.rightchoice .selected').attr('id').substr(1)
		
		$.ajax({
			url: "rapotron.php?rapper1=" + r1 +"&rapper2=" + r2,
			method: "GET",
			success: function(resp) {
				r = JSON.parse(resp)
				$('#punchline').text(r.punchline)
				$('#auteurs').text(r.authors)
			},
			error: function(resp) {
				$('#punchline').text("Erreur")
				$('#auteurs').text("Erreur")
			}
		})
	}
	

})