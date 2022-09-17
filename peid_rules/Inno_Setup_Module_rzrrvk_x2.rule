rule _Inno_Setup_Module_rzrrvk
{
	meta:
		description = "Inno Setup Module"
	strings:
		$a = {496E6E6F}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
