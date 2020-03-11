# Extract test name and test per second from test plan.
with open('ScaleModel_SingleAPI_New.csv', 'w') as fw:
    with open('ScaleModel_SingleAPI_New.txt', 'r') as f:
        for line in f.readlines():
            # print(line)
            #type(line)
            ptn=r'<TestProfile Name="(\w*)".*Percentage="(.*)" Type=.*'
            result = re.findall(ptn,line)
            if (len(result) != 0):
                fw.write(str(result).replace("[","").replace("]","").replace("(","").replace(")","").replace("'",""))
                fw.write("\n")

# props.put("RPSTimes", "1");
# double rpmPerThreads = 60.0 / (3 * ${apiCount});

# int {name}_Threads = (int)Math.ceil(${{name}_baselineTPS} * ${devicesCount} / ${agentCount} /rpmPerThreads);
# double {name}_TPS = ${{name}_baselineTPS} * ${devicesCount} / ${agentCount};
# props.put("TC201800001_Napa_DVR_WatchAndTricks_TPS", String.valueOf(TC201800001_Napa_DVR_WatchAndTricks_TPS));
# int totalThreads = TC201800001_Napa_DVR_WatchAndTricks_Threads + ...
# props.put("totalThreads", String.valueOf(totalThreads));

with open('TestTPMCalculateCode.txt', 'w') as fw:
    fw.write(f'props.put("RPSTimes", "1");\n')
    fw.write(f'double rpmPerThreads = 60.0 / (3 * ${{apiCount}});\n')
    totalThreadsStr = 'int totalThreads = '
    with open('TestName.txt', 'r') as f:
        for name in f.readlines():
            if (len(name)) :
                name = name.replace('\n', '')
                totalThreadsStr += name+'_Threads'
                totalThreadsStr += ' + '
                # fw.write(f'int {name}_Threads = (int)Math.ceil(${{{name}_baselineTPM}} * ${{devicesCount}} / ${{agentCount}} /rpmPerThreads);')
                fw.write(f'int {name}_Threads = (int)Math.ceil(${{{name}_baselineTPS}} * 60 / ${{agentCount}} /rpmPerThreads);') # oss
                fw.write('\n')
                # fw.write(f'double {name}_TPM = ${{{name}_baselineTPM}} * ${{devicesCount}} / ${{agentCount}};')
                fw.write(f'double {name}_TPS = ${{{name}_baselineTPS}} * 60 / ${{agentCount}};') # oss
                fw.write('\n')
                fw.write(f'props.put("{name}_Threads", String.valueOf({name}_Threads));')
                fw.write('\n')
                fw.write(f'props.put("{name}_TPS", String.valueOf({name}_TPS));')
                fw.write('\n')
    print(totalThreadsStr)
    fw.write(totalThreadsStr[:-3]+';\n')
    fw.write(f'props.put("totalThreads", String.valueOf(totalThreads));')


# props.put("RPSTimes", "1");
# Double rpsTime = 0.1;
# int rampUpTime = Integer.parseInt(vars.get("Rampup"));
# if(rampUpTime > 100)
# {	
# 	//rpsTime=0.01*rpsTime;
# Double TC201800001_Napa_DVR_WatchAndTricks_TPS = Double.parseDouble(props.get("TC201800001_Napa_DVR_WatchAndTricks_TPS")) * rpsTime;
# props.put("TC201800001_Napa_DVR_WatchAndTricks_TPS", String.valueOf(TC201800001_Napa_DVR_WatchAndTricks_TPS));
with open('TestTPMRampupCode.txt', 'w') as fw:
    fw.write(f'props.put("RPSTimes", "1");\n')
    fw.write(f'Double rpsTime = 0.1;\n')
    fw.write(f'int rampUpTime = Integer.parseInt(vars.get("Rampup"));\n')
    fw.write(f'if(rampUpTime > 100)\n')
    fw.write(f'{{\n')
    with open('TestName.txt', 'r') as f:
        for name in f.readlines():
            if (len(name)) :
                name = name.replace('\n', '')
                # fw.write(f'int {name}_Threads = (int)Math.ceil(${{{name}_baselineTPM}} * ${{devicesCount}} / ${{agentCount}} /rpmPerThreads);')
                fw.write(f'Double {name}_TPM = Double.parseDouble(props.get("{name}_TPM")) * rpsTime;\n')
                fw.write(f'props.put("{name}_TPM", String.valueOf({name}_TPM));\n')
    fw.write(f'}}\n')
