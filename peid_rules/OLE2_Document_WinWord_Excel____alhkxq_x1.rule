rule _OLE2_Document_WinWord_Excel____alhkxq
{
	meta:
		description = "OLE2 Document _WinWord_ Excel ____"
	strings:
		$a = {D0CF11E0A1B11AE1}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
