rule _eXPressor_1_2_0_Beta_PE_Packer_ceahpq
{
	meta:
		description = "eXPressor 1_2_0 Beta PE Packer"
	strings:
		$a = {558BEC81EC????????535657EB??457850722D762E312E322E2E}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
