rule __PseudoSigner_0_2_Video_Lan_Client_ekkvyp
{
	meta:
		description = "_ PseudoSigner 0_2 _Video_Lan_Client"
	strings:
		$a = {5589E583EC08909090909090909090909090909001FFFF0101010001909090909090909090909090909000010001000190900001}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
