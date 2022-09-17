rule __PseudoSigner_0_1_PE_Protect_0_9_oqyrqh
{
	meta:
		description = "_ PseudoSigner 0_1 _PE Protect 0_9"
	strings:
		$a = {525155576467A1300085C0780DE8070000005883C007C690C3E9}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
