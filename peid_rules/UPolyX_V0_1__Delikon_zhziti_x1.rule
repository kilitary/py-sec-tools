rule _UPolyX_V0_1__Delikon_zhziti
{
	meta:
		description = "UPolyX V0_1 __ Delikon"
	strings:
		$a = {E2??FF??0000000000000000000000000000}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
