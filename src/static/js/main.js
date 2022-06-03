const PACIENTE_NIÑO = 1;
const PACIENTE_JOVEN = 2;
const CGI = 2;
const PACIENTE_ANCIANO = 3
var es_fumador = 0;
var tiene_dieta = 0;
var tipoPaciente = 0;
var pacientePorConsulta = 0;
var pacientesCola = 0;
var pacienteSeleccionado = 3;
var box_disponibles = 0;
var estadoConsulta = '';

$( document ).ready(function() {
    getPacientesPorConsulta(3)
    setTituloTablaAtenciones('Urgencia')
    getPacientes()
    getPacientesUrgencia()
    getConsultas()
    getEstadoConsulta(3)
    setTableTipoPaciente('Urgencia',3)

    $(".cerrarModal").click(function(){
        $(".form-modal").modal('hide')
    });

    $("#formularioNuevoPaciente").on('submit', function(event){
        paciente = $("#listPacienteid").val()
        tipoPaciente = paciente == PACIENTE_ANCIANO ? CGI : paciente
        event.preventDefault();
        $.ajax({
            type:"POST",
            url: "/enviaDatos",
            data:{
                idHistoriaClinica : $("#idHistoriaClinica").val(),
                nombres:$("#nombrePaciente").val(),
                apellidos:$("#apellidoPaciente").val(),
                telefono:$("#telefonoPaciente").val(),
                email:$("#emailPaciente").val(),
                tipoPaciente:tipoPaciente,
                edad:$("#edadPaciente").val(),
                peso:$("#pesoPaciente").val(),
                estatura:$("#estaturaPaciente").val(),
                es_fumador :es_fumador,
                tiempoFumador : $("#tiempoFumador").val(),
                dieta : tiene_dieta
            },
            success:function(response){
                if(response == "OK"){
                    getPacientes()
                    messageAlert("Se ha creado el paciente correctamente.", 'success')
                }
                $(".form-modal").modal('hide')
            },
            error:function(response){
                messageAlert("Ha ocurrido un error al crear al paciente.", 'success')
            }
        })
    })
});

let openModalNuevoPaciente =() =>{
    $('#modalFormPaciente').modal('show')
}

let activarLiberar = () => {
    if(pacientesCola > 0){
        $("#liberarConsulta").removeAttr('disabled');
    }else if(pacientesCola == 0){
        $("#liberarConsulta").prop( "disabled", true );
        //$("#liberarConsulta").attr('disabled');
    }
}

let messageAlert = (text, icon) => {
    let titulo = icon == 'error' ? '¡Ups ha ocurrido un error!' : '¡Proceso existoso!';
    Swal.fire({
      title: titulo,
      text:text,
      icon: icon,
      confirmButtonColor: '#3085e3',
      confirmButtonText: 'Aceptar'
    })
  }

let changePaciente = () => {
  let idTipoPaciente = $("#listPacienteid").val()
  if(idTipoPaciente  == PACIENTE_JOVEN){
    activaFumador();
  }else if(idTipoPaciente == PACIENTE_ANCIANO){
    activaAnciano()
  }else{
    $(".child-class").css("display", "block")
    $(".dieta-class").css("display", "none")
    $(".fumador-class").css("display", "none")
  }
}

let activaFumador = () =>{
    $(".child-class").css("display", "none")
    $(".dieta-class").css("display", "none")
    $(".fumador-class").css("display", "block")
}

let activaAnciano = () =>{
    $(".child-class").css("display", "none")
    $(".dieta-class").css("display", "block")
    $(".fumador-class").css("display", "none")
}

let desbloquearFumador = (event) => {
    if(event.target.value != 'NO'){
        es_fumador = 1;
        $(".tiempoFumador").removeAttr('disabled')
    }else{
        es_fumador = 0;
        $(".tiempoFumador").val("")
        $(".tiempoFumador").attr('disabled', true)
    }
}

let desbloquearDieta = (event) => {
    if(event.target.value != 'NO'){
        tiene_dieta = 1;
    }else{
        tiene_dieta = 0;
    }
}


let getPacientes = () => {
    $.ajax({
        type:"POST",
        url: "/getPacientes",
        data:{},
        success:function(response){
            crearTablaPacientes(response)
        },
        error:function(response){
        }
    })
}

let getPacientesNiños = () => {
    pacienteSeleccionado = 1;
    $.ajax({
        type:"POST",
        url: "/getPacientesNinos",
        success:function(response){
            crearTablaAtenciones(response)
        },
        error:function(response){
        }
    })
}

let getPacientesCGI = () => {
    pacienteSeleccionado = 2;
    $.ajax({
        type:"POST",
        url: "/getPacientesCGI",
        success:function(response){
            crearTablaAtenciones(response)
        },
        error:function(response){
        }
    })
}

let getPacientesUrgencia = () => {
    pacienteSeleccionado = 3;
    $.ajax({
        type:"POST",
        url: "/getPacientesUrgencia",
        success:function(response){
            crearTablaAtenciones(response)
        },
        error:function(response){
        }
    })
}

let  empty_row = (id_table, msg) =>{
    let tabla = $(`#${id_table}`);
    $(`#${id_table} tbody`).empty();
    let tr = "<tr>";
     tr += "<td class='text-center' colspan='12'>"+msg; 
     tr += "</tr>"; 
     tabla.append(tr);
  }


let crearTablaAtenciones = (data) =>{
    let tbl = $("#tblDashboard");
    if(data == ""){
        empty_row(tbl[0].id,'No hay datos en esta tabla')
        return
    }

    let tabla = $("#tblDashboard tbody");
    $("#tblDashboard tbody").empty();
    let tr = "";
    $.each(data, function (ind, elem){
        tr += '<tr>'
        let idPaciente = 0
        $.each(elem, function (ind, dato){
            if(ind != 5 && ind != 6 && ind != 7 && ind != 9 && ind != 10){
                tr += "<td>"+dato+"</td>";
            }
            
            if(ind == 0){
                idPaciente = dato
            }

            if(ind == 9){
                if(dato == 2){
                    pacientesCola = pacientesCola + 1;
                }
            }
        })
        tr += `<td align='left'>
                <button class="btn btn-link text-info" onclick='atenderPaciente(${idPaciente},2,${pacienteSeleccionado} )' title="Atender"><i class="fa fa-arrow-circle-right" style="font-size:24px" aria-hidden="true"></i>
                </button>
        </td>`;
        tr += "</tr>"; 
    })
    tabla.append(tr);
    activarLiberar()
}


let getConsultas = () => {
    $.ajax({
        type:"POST",
        url: "/getConsultas",
        success:function(response){ 
            crearTablaConsultas(response)
        },
        error:function(response){
        }
    })
}

let crearTablaConsultas = (data) =>{
    let tbl = $("#tblConsultas");
    if(data == ""){
        empty_row(tbl[0].id,'No hay datos en esta tabla')
        return
    }
    $("#tblConsultas tbody").empty();
    let tabla = $("#tblConsultas tbody");
    let tr = "";
    $.each(data, function (ind, elem){
        tr += '<tr>'
        $.each(elem, function (ind, dato){
            tr += "<td>"+dato+"</td>";
        })
        tr += `<td align='left'>
                    <button class="btn btn-link text-info" title="Liberar Consulta" onclick='verFichaPaciente()'>
                        <i class="fa fa-check-circle" style="font-size:24px" aria-hidden="true"></i>
                    </button>
                    <button class="btn btn-link text-warning" title="Cambiar cantidad pacientes" onclick='verFichaPaciente()'>
                        <i class="fa fa-pencil-square" style="font-size:24px" aria-hidden="true"></i>
                    </button>
                </td>`;
        tr += "</tr>";
    })
    tabla.append(tr);
}

let getPacientesPorConsulta = (idConsulta) => {
    $.ajax({
        type:"POST",
        url: "/getPacientesPorConsulta",
        data: {'idConsulta':idConsulta},
        success:function(response){
            pacientePorConsulta = response
        },
        error:function(response){
        }
    })
}

let validaPacienteConsulta = () =>{
    return pacientePorConsulta < (pacientesCola +1) ?  false : true
}

let updateEstadoConsulta = (idConsulta) => {
    let estado = 6
    if((pacientePorConsulta - (pacientesCola + 1))  == 0 ){
        estado = 4
    }
    $.ajax({
        type:"POST",
        url: "/updateEstadoConsulta",
        data: {'idConsulta':idConsulta, 'estado': estado},
        success:function(response){
            getEstadoConsulta(pacienteSeleccionado)
            messageAlert("El paciente esta en atencion.", 'success')
        },
        error:function(response){
        }
    })
}

let getEstadoConsulta = () => {
    $.ajax({
        type:"POST",
        url: "/getEstadoConsulta",
        data: {'consulta':pacienteSeleccionado},
        success:function(response){
            $("#estadoConsulta").text(response[0])
            estadoConsulta = response[0]
        },
        error:function(response){
        }
    })
}

let atenderPaciente = (idPaciente, idEstado, pacienteSeleccionado) =>{
    console.log(idPaciente, idEstado, pacienteSeleccionado)
    if(estadoConsulta == 'Consulta ocupada'){
        messageAlert("Debe liberar la consulta antes de antender al paciente.", 'error')
        return;
    }
    let valido = validaPacienteConsulta()
    if(valido){
        $.ajax({
            type:"POST",
            url: "/atenderPaciente",
            data:{'idPaciente':idPaciente, 'idEstado':idEstado, 'consulta':pacienteSeleccionado},
            success:function(response){
                if(pacienteSeleccionado == 1){
                    getPacientesNiños()
                }else if(pacienteSeleccionado == 2){
                    getPacientesCGI()
                }else{ 
                    getPacientesUrgencia()
                }
                console.log(pacienteSeleccionado)
                updateEstadoConsulta(pacienteSeleccionado,valido)
                pacientesCola = 0; 
            },
            error:function(response){
            }
        })
    }else{
        messageAlert("Debe liberar la consulta antes de antender al paciente.", 'error')
    }
}


let setTableTipoPaciente = (nombreTipoPaciente, idTipoPaciente = 0) => {
    setTituloTablaAtenciones(nombreTipoPaciente)
    pacientesCola = 0;
    if(idTipoPaciente === 1){
        getPacientesNiños();
    }else if(idTipoPaciente === 2){
        getPacientesCGI();
    }else{
        getPacientesUrgencia();
    }
    console.log(idTipoPaciente)
    getEstadoConsulta(idTipoPaciente)
    getPacientesPorConsulta(idTipoPaciente);
}


let crearTablaPacientes = (data) => {
    let tbl = $("#tablePacientes");
    if(data == ""){
        empty_row(tbl[0].id,'No hay datos en esta tabla')
        return
    }
    
    $("#tablePacientes tbody").empty();
    let tabla = $("#tablePacientes tbody");
    let tr = "";
    $.each(data, function (ind, elem){
        tr += '<tr>'
        let idPaciente = 0
        $.each(elem, function (ind, dato){
            tr += "<td>"+dato+"</td>";
            if(ind == 0){
                idPaciente = dato
            }
        })
        tr += `<td align='left'>
                    <button class="btn btn-link text-info" onclick='verFichaPaciente(${idPaciente})'>
                        <i class="fa fa-user-circle" style="font-size:24px" aria-hidden="true"></i>
                    </button>
                    <button class="btn btn-link text-warning" onclick='verFichaPaciente(${idPaciente})'>
                        <i class="fa fa-pencil-square" style="font-size:24px" aria-hidden="true"></i>
                    </button>
                    <button  class="btn btn-link text-danger" onclick='verFichaPaciente(${idPaciente})'>
                        <i class="fa fa-ban" style="font-size:24px" aria-hidden="true"></i>
                    </button>
            </td>`;
        tr += "</tr>"; 
      });
     tabla.append(tr);
}

let verFichaPaciente = (id) => {
    messageAlert("Esta funcion no ha sido desarrollada", "error")
}

let updatePacientesTotalConsultas = () => {
    
}

let liberarConsulta = () => {
    $.ajax({
        type:"POST",
        url: "/liberarConsulta",
        data: {'consulta':pacienteSeleccionado ,'estado':3},
        success:function(response){
            if(pacienteSeleccionado === 1){
                getPacientesNiños();
            }else if(pacienteSeleccionado === 2){
                getPacientesCGI();
            }else{
                getPacientesUrgencia();
            }
            getEstadoConsulta(pacienteSeleccionado)
            getPacientesPorConsulta(pacienteSeleccionado);
            pacientesCola = 0
            messageAlert("Se ha Liberado la consulta", "success")
        },
        error:function(response){
        }
    })
}

let setTituloTablaAtenciones = (tipoResumen) => {

    $(".titulo-resumen").text('Resumen Atencion Consulta '+tipoResumen)
    
}