import { exec } from 'child_process';
import { readdirSync, statSync } from 'fs';
import { join } from 'path';

function getJavaScriptFiles(dir) {
    let jsFiles = [];
    const files = readdirSync(dir);

    for (const file of files) {
        const fullPath = join(dir, file);
        if (statSync(fullPath).isDirectory()) {
            jsFiles = jsFiles.concat(getJavaScriptFiles(fullPath));
        } else if (fullPath.endsWith('.js')) {
            jsFiles.push(fullPath);
        }
    }

    return jsFiles;
}

const jsFiles = getJavaScriptFiles('./xrwvm-fullstack_developer_capstone/server/database');

jsFiles.forEach(file => {
    exec(`jshint "${file}"`, (error, stdout, stderr) => {
        if (stderr.trim()) {
            console.error(`Error linting ${file}: ${stderr.trim()}`);
        } else if (stdout.trim()) {
            console.log(`Warnings/Notes for ${file}:\n${stdout.trim()}`);
        } else {
            console.log(`Linted: ${file} (No issues found)`);
        }
    });
});

console.log('Linting complete.');
