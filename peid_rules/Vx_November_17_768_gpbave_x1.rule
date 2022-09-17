rule _Vx_November_17_768_gpbave
{
	meta:
		description = "Vx_ November 17_768"
	strings:
		$a = {E8????5E81EE????5033C08ED8803E??????0E1F????FC}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
