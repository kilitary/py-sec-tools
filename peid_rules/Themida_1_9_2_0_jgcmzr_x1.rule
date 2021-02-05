rule _Themida_1_9_2_0_jgcmzr
{
	meta:
		description = "Themida 1_9_2_0"
	strings:
		$a = {BE????BF????B9????56FCF3A55FE9}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
