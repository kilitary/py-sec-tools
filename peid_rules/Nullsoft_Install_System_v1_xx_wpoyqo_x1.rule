rule _Nullsoft_Install_System_v1_xx_wpoyqo
{
	meta:
		description = "Nullsoft Install System v1_xx"
	strings:
		$a = {505351521E069CB82135CD2153BB????26????49485B}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
