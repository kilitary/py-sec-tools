rule _Borland_Graphics_Interface_Driver_fxpklk
{
	meta:
		description = "Borland Graphics Interface Driver"
	strings:
		$a = {46424744}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
