rule _SoftProtect__SoftProtect_by_ru_lnthta
{
	meta:
		description = "SoftProtect __ SoftProtect_by_ru"
	strings:
		$a = {E80C1500008D852F140000C70000000000E8290F0000E8F61400008D852001000050E8AA16000083}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
