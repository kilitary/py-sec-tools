rule _X_PEOR_v0_99b_zflmfg
{
	meta:
		description = "X_PEOR v0_99b"
	strings:
		$a = {E8????????5D8BCD81ED7A2940??89AD0F6D40}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
