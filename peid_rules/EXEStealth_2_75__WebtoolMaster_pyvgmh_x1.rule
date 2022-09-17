rule _EXEStealth_2_75__WebtoolMaster_pyvgmh
{
	meta:
		description = "EXEStealth 2_75 __ WebtoolMaster"
	strings:
		$a = {33C9B44ECD217302FF??BA??00B8??3DCD21}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
