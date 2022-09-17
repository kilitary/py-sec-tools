rule _PEArmor_V0_7X__Hying_kjhbyc
{
	meta:
		description = "PEArmor V0_7X __ Hying"
	strings:
		$a = {609C64FF3500000000E879010000900000000000000000000000????????????????0000000000000000000000000000000000000000}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
