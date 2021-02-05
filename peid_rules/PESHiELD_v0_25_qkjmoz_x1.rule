rule _PESHiELD_v0_25_qkjmoz
{
	meta:
		description = "PESHiELD v0_25"
	strings:
		$a = {60E82B000000}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
