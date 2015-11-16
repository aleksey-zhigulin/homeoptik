/**
 * Created by aleksey on 11/10/15.
 */

//change left eye
$('#OS_SPH, #OS_CYL, #OS_AX, #OS_PD').change(function (){
    var receipt = Cookies.getJSON('Receipt');
    var param = $(this).prop('id').split('_')[1];
    receipt['OS'][param] = $(this).val();

    //change right eye if equal
    var checked = $('#OD_OS').prop('checked');
    if (checked) {
        receipt['OD'][param] = receipt['OS'][param];
        $('#OD_'+param).val(receipt['OD'][param]);
    }

    Cookies.set('Receipt', receipt);
    updateReceiptForm();
})

//change right eye
$('#OD_SPH, #OD_CYL, #OD_AX, #OD_PD').change(function (){
    var receipt = Cookies.getJSON('Receipt');
    var param = $(this).prop('id').split('_')[1];
    receipt['OD'][param] = $(this).val();
    Cookies.set('Receipt', receipt);
    updateReceiptForm();
})

//click equal
$('#OD_OS').change(function (){
    var receipt = Cookies.getJSON('Receipt');
    var checked = $(this).prop('checked');
    var fieldset = $(this).parent().next('fieldset');

    if (checked) {
        receipt['OD'] = receipt['OS'];
        receipt['OD=OS'] = true;
        $('#OD_SPH').val(receipt['OD']['SPH']);
        $('#OD_CYL').val(receipt['OD']['CYL']);
        $('#OD_AX').val(receipt['OD']['AX']);
        $('#OD_PD').val(receipt['OD']['PD']);
        fieldset.prop('disabled', true);
    } else {
        receipt['OD=OS'] = false;
        fieldset.prop('disabled', false);
    }
    Cookies.set('Receipt', receipt);
    updateReceiptForm();

})

window.onload = function (){
    var receipt = Cookies.getJSON('Receipt');
    if (typeof(receipt) == 'undefined') {
        receipt = {
            'OS': {'SPH': $('#OS_SPH').val(),'CYL': $('#OS_CYL').val(), 'AX': $('#OS_AX').val(), 'PD': $('#OS_PD').val()},
            'OD': {'SPH': $('#OD_SPH').val(),'CYL': $('#OD_CYL').val(), 'AX': $('#OD_AX').val(), 'PD': $('#OD_PD').val()},
            'OD=OS': $('#OD_OS').prop('checked')
        }
        Cookies.set('Receipt', receipt);
    } else {

        //left eye
        var OS = receipt['OS'];
        if (OS['SPH']) {
            $('#OS_SPH').val(OS['SPH']);
        }
        if (OS['CYL']) {
            $('#OS_CYL').val(OS['CYL']);
        }
        if (OS['AX']) {
            $('#OS_AX').val(OS['AX']);
        }
        if (OS['PD']) {
            $('#OS_PD').val(OS['PD']);
        }

        //equal
        var OD;
        var fieldset = $("#OD_OS").parent().next('fieldset');
        if (receipt['OD=OS']) {
            $('#OD_OS').prop('checked', true);
            fieldset.prop('disabled', true);
            OD = OS;
        } else {
            $('#OD_OS').prop('checked', false);
            fieldset.prop('disabled', false);
            OD = receipt['OD'];
        }

        //right eye
        if (OD['SPH']) {
            $('#OS_SPH').val(OD['SPH']);
        }
        if (OD['CYL']) {
            $('#OS_CYL').val(OD['CYL']);
        }
        if (OD['AX']) {
            $('#OS_AX').val(OD['AX']);
        }
        if (OD['PD']) {
            $('#OS_PD').val(OD['PD']);
        }

    }
    updateReceiptForm();
};

function updateReceiptForm() {
    var receipt = Cookies.getJSON('Receipt');
    if (receipt['OD=OS']) {
        $('#id_quantity').val(2);
        $('#id_recept').val('OS=OD: SPH('+receipt.OS.SPH+'), CYL('+receipt.OS.CYL+'), AX('+receipt.OS.AX+'), PD('+receipt.OS.PD+')');
    } else {
        $('#id_quantity').val(2);
        $('#id_recept').val(
            'OS: SPH('+receipt.OS.SPH+'), CYL('+receipt.OS.CYL+'), AX('+receipt.OS.AX+'), PD('+receipt.OS.PD+'); ' +
            'OD: SPH('+receipt.OD.SPH+'), CYL('+receipt.OD.CYL+'), AX('+receipt.OD.AX+'), PD('+receipt.OD.PD+')');
    }
}