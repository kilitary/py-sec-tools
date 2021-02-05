rule __PseudoSigner_0_1_Code_Lock_swogfb
{
	meta:
		description = "_ PseudoSigner 0_1 _Code_Lock"
	strings:
		$a = {434F44452D4C4F434B2E4F435800012801504B47054C3FB4044D4C474BE9}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
