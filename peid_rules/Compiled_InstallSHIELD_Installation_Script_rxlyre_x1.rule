rule _Compiled_InstallSHIELD_Installation_Script_rxlyre
{
	meta:
		description = "Compiled InstallSHIELD Installation Script"
	strings:
		$a = {B8C90C00}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
