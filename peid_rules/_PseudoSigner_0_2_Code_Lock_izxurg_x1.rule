rule __PseudoSigner_0_2_Code_Lock_izxurg
{
	meta:
		description = "_ PseudoSigner 0_2 _Code_Lock"
	strings:
		$a = {434F44452D4C4F434B2E4F435800012801504B47054C3FB4044D4C474B}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
