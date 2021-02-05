rule _EXE2COM_Method_1__uvshxr
{
	meta:
		description = "EXE2COM _Method 1_"
	strings:
		$a = {8CDBBE????8BC6B1??D3E803C303????A3????8CC805????A3}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
