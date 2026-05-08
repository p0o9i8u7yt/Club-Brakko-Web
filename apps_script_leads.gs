// ============================================================
// GOOGLE APPS SCRIPT - Club Brakko Leads
// Pegar este código en: Extensions > Apps Script
// dentro del Google Sheet "Leads Club Brakko"
// ============================================================

const SHEET_NAME = "Leads"; // Nombre de la hoja dentro del documento

function doPost(e) {
  try {
    var sheet = SpreadsheetApp.getActiveSpreadsheet().getSheetByName(SHEET_NAME);

    // Si la hoja no existe, crearla
    if (!sheet) {
      sheet = SpreadsheetApp.getActiveSpreadsheet().insertSheet(SHEET_NAME);
    }

    // Si es la primera fila, agregar encabezados
    if (sheet.getLastRow() === 0) {
      sheet.appendRow(["Fecha", "Nombre", "Teléfono", "Email"]);
    }

    // Obtener los datos (priorizando parámetros de formulario)
    var data = e.parameter;
    
    // Si no hay parámetros (fallback por si acaso)
    if (!data.Nombre && e.postData && e.postData.contents) {
      try {
        data = JSON.parse(e.postData.contents);
      } catch(i) {}
    }

    // Agregar la fila con los datos del lead
    sheet.appendRow([
      data.Fecha || new Date().toLocaleString("es-AR"),
      data.Nombre || "Sin nombre",
      data.Telefono || "Sin teléfono",
      data.Email || "Sin email"
    ]);

    return ContentService
      .createTextOutput(JSON.stringify({ result: "success" }))
      .setMimeType(ContentService.MimeType.JSON);

  } catch (err) {
    return ContentService
      .createTextOutput(JSON.stringify({ result: "error", error: err.toString() }))
      .setMimeType(ContentService.MimeType.JSON);
  }
}

// Función GET para verificar que el script está activo (test)
function doGet(e) {
  return ContentService
    .createTextOutput(JSON.stringify({ status: "Club Brakko Leads script activo ✅" }))
    .setMimeType(ContentService.MimeType.JSON);
}
