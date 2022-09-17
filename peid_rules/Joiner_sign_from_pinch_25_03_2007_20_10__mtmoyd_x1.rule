rule _Joiner_sign_from_pinch_25_03_2007_20_10__mtmoyd
{
	meta:
		description = "Joiner _sign from pinch 25_03_2007 20_10_"
	strings:
		$a = {0FC80FCFC6C48B0FACEA990FADD813F50FBDEF85EF85DA69FE????????21F9BE????????23CF0FBCFED2DC85EFB9????????C6C0F78D35????????8D0D}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
