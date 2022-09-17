rule _Microsoft_C_v1_04_zqtyoz
{
	meta:
		description = "Microsoft C v1_04"
	strings:
		$a = {FAB8????8ED88ED0268B??????2BD8F7??????75??B104D3E3EB}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
