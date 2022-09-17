rule _AVP_Antiviral_Database_oxblwm
{
	meta:
		description = "AVP Antiviral Database"
	strings:
		$a = {41565020416E7469766972616C204461746162617365}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
