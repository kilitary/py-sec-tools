rule _WinRAR_32_bit_SFX_Module_zvmymj
{
	meta:
		description = "WinRAR 32_bit SFX Module"
	strings:
		$a = {E9????0000000000000000}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
