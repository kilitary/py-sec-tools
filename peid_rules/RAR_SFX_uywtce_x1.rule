rule _RAR_SFX_uywtce
{
	meta:
		description = "RAR SFX"
	strings:
		$a = {E8????????50E8????????0000000090}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
