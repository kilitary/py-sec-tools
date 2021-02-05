rule _Guardant_Stealth_aka_Novex_Dongle_odimqv
{
	meta:
		description = "Guardant Stealth aka Novex Dongle"
	strings:
		$a = {558BEC83C4F060E851FFFFFF}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
