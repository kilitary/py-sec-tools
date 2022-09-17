rule _Inno_Setup_Module_v1_09a_esxlrt
{
	meta:
		description = "Inno Setup Module v1_09a"
	strings:
		$a = {558BEC83C4C053565733C08945F08945C48945C0E8A77FFFFFE8FA92FFFFE8F1B3FFFF33C0}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
