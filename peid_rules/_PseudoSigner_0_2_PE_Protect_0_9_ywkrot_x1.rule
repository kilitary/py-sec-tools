rule __PseudoSigner_0_2_PE_Protect_0_9_ywkrot
{
	meta:
		description = "_ PseudoSigner 0_2 _PE Protect 0_9"
	strings:
		$a = {525155576467A1300085C0780DE8070000005883C007C690C3}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
