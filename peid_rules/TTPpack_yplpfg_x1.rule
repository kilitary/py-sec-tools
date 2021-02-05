rule _TTPpack_yplpfg
{
	meta:
		description = "TTPpack"
	strings:
		$a = {E8000000005D81EDF58F40006033F6E8110000008B642408648F05}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
