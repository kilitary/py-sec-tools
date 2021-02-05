rule _ASProtect_v1_2x_clcedk
{
	meta:
		description = "ASProtect v1_2x"
	strings:
		$a = {0042CD217231B96E0333D2B440CD2172193BC17515B80042}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
