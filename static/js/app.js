(function($) {
	function lang(lang) {
		var dicts = {
			username: "Cedula",
			password: "Contraseña",
			first_name: "Nombre",
			last_name: "Primer apellido",
			email: "Correo",
			password_confirm: "Confirmar contraseña"
		};
		return dicts[lang];
	}
	$(function() {
		$("label[for='id_username']")
			.closest("label")
			.text(lang("username"));
		$("label[for='id_password']")
			.closest("label")
			.text(lang("password"));
		$("label[for='id_first_name']")
			.closest("label")
			.text(lang("first_name"));
		$("label[for='id_last_name']")
			.closest("label")
			.text(lang("last_name"));
		$("label[for='id_email']")
			.closest("label")
			.text(lang("email"));
		$("label[for='id_password1']")
			.closest("label")
			.text(lang("password"));
		$("label[for='id_password2']")
			.closest("label")
			.text(lang("password_confirm"));
		$("#id_password1").addClass("form-control");
		$("#id_password2").addClass("form-control");

		[
			"#pacientes_tbl",
			"#observaciones_tbl",
			"#tests_tbl",
			"#examenes_tbl",
			"#habits_tbl",
			"#lipidicos_tbl"
		].forEach(function(table) {
			$(table).DataTable({
				language: {
					sProcessing: "Procesando...",
					sLengthMenu: "Mostrar _MENU_ registros",
					sZeroRecords: "No se encontraron resultados",
					sEmptyTable: "Ningún dato disponible en esta tabla",
					sInfo:
						"Mostrando registros del _START_ al _END_ de un total de _TOTAL_ registros",
					sInfoEmpty:
						"Mostrando registros del 0 al 0 de un total de 0 registros",
					sInfoFiltered: "(filtrado de un total de _MAX_ registros)",
					sInfoPostFix: "",
					sSearch: "Buscar:",
					sUrl: "",
					sInfoThousands: ",",
					sLoadingRecords: "Cargando...",
					oPaginate: {
						sFirst: "Primero",
						sLast: "Último",
						sNext: "Siguiente",
						sPrevious: "Anterior"
					},
					oAria: {
						sSortAscending:
							": Activar para ordenar la columna de manera ascendente",
						sSortDescending:
							": Activar para ordenar la columna de manera descendente"
					}
				}
			});
		});

		$('.datepicker').datepicker({language: 'es-ES'});
		$('.datepicker-register').datepicker({language: 'es-ES', format:"yyyy-mm-dd"});

		$('#hamburguesa').on('click', function() {
			$('#mobile-menu-content').addClass('open');
		})

		$('.close-submenu-mobile').on('click', function () {
			$('#mobile-menu-content').removeClass('open');
		})

		let alto = $(window).height();
		let content = jQuery('#content').height();
		if (content <= alto) {
			$('#content').attr("style","min-height:" + (alto - 150) + "px");
			$('#footer').attr("style","background-color:#41B6A6");
		} else {
			$('#footer').attr("style","background-color:#41B6A6");
		}
	});
})(jQuery);
