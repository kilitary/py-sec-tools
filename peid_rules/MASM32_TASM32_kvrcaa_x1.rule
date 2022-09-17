rule _MASM32_TASM32_kvrcaa
{
	meta:
		description = "MASM32  TASM32"
	strings:
		$a = {2BC050E8}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
