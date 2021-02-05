rule _RAR_SFX_mdvvfv
{
	meta:
		description = "RAR SFX"
	strings:
		$a = {E8????????50E8????????0000000090}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
